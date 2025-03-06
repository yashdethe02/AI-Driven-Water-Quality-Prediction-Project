import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls';

const Water3D = ({ qualityData }) => {
  const mountRef = useRef(null);
  
  useEffect(() => {
    // Scene setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, mountRef.current.clientWidth/mountRef.current.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    
    // Water surface geometry
    const waterGeometry = new THREE.PlaneGeometry(100, 100, 50, 50);
    const material = new THREE.MeshPhongMaterial({
      color: 0x006994,
      transparent: true,
      opacity: 0.8
    });
    
    // Animate surface waves
    const waterSurface = new THREE.Mesh(waterGeometry, material);
    waterSurface.rotation.x = -Math.PI / 2;
    scene.add(waterSurface);

    // Add contamination markers
    qualityData.forEach(point => {
      const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(0.5),
        new THREE.MeshBasicMaterial({ 
          color: new THREE.Color().setHSL(0.1, 1, 0.5 * point.contamination) 
        })
      );
      sphere.position.set(point.x, 0, point.y);
      scene.add(sphere);
    });

    // Lighting
    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    // Camera controls
    const controls = new TrackballControls(camera, renderer.domElement);
    
    // Responsive handling
    const handleResize = () => {
      camera.aspect = mountRef.current.clientWidth / mountRef.current.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(mountRef.current.clientWidth, mountRef.current.clientHeight);
    };
    
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [qualityData]);

  return <div ref={mountRef} style={{ width: '100%', height: '70vh' }} />;
};